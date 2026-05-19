import json
from typing import Any

import pandas as pd
from utils.logging import get_logger

logger = get_logger(__name__)

NO_GENRE = "(no genres listed)"


def _parse_genres(raw: str | float) -> list[str]:
    if pd.isna(raw) or not str(raw).strip():
        return []
    genres = [g.strip() for g in str(raw).split("|") if g.strip()]
    return [] if genres == [NO_GENRE] else genres


def _rating_stats(ratings: pd.DataFrame) -> pd.DataFrame:
    return (
        ratings.groupby("movieId", as_index=False)
        .agg(average_rating=("rating", "mean"), ratings_count=("rating", "count"))
    )


def _tags_by_movie(tags: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        tags.groupby("movieId")["tag"]
        .apply(lambda values: sorted({str(v).strip() for v in values if pd.notna(v)}))
        .reset_index(name="tags")
    )
    return grouped


def transform(data: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    movies = data["movies"].copy()

    if "ratings" in data:
        movies = movies.merge(_rating_stats(data["ratings"]), on="movieId", how="left")
    else:
        movies["average_rating"] = 0.0
        movies["ratings_count"] = 0

    if "tags" in data:
        movies = movies.merge(_tags_by_movie(data["tags"]), on="movieId", how="left")
    else:
        movies["tags"] = [[] for _ in range(len(movies))]

    documents: list[dict[str, Any]] = []
    for row in movies.itertuples(index=False):
        movie_id = int(row.movieId)
        avg = float(row.average_rating) if pd.notna(row.average_rating) else 0.0
        count = int(row.ratings_count) if pd.notna(row.ratings_count) else 0
        tag_list = list(row.tags) if isinstance(row.tags, list) else []

        documents.append(
            {
                "id": str(movie_id),
                "title": str(row.title),
                "genres": _parse_genres(row.genres),
                "tags": tag_list,
                "average_rating": round(avg, 2),
                "ratings_count": count,
            }
        )

    logger.info("Transformed %d movie documents", len(documents))
    return documents


def documents_to_jsonl(documents: list[dict[str, Any]]) -> str:
    return "\n".join(json.dumps(doc, ensure_ascii=False) for doc in documents)
