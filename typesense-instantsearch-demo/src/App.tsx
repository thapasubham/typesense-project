import React from 'react';
import TypesenseInstantSearchAdapter from 'typesense-instantsearch-adapter';

import {
  Configure,
  DynamicWidgets,
  RefinementList,
  Hits,
  InstantSearch,
  Pagination,
  SearchBox,
} from 'react-instantsearch';

import type { Hit } from 'instantsearch.js';

import './App.css';

const typesenseInstantsearchAdapter = new TypesenseInstantSearchAdapter({
  server: {
    apiKey: 'xyz',
    nodes: [
      {
        host: 'localhost',
        port: 8108,
        protocol: 'http',
      },
    ],
  },

  additionalSearchParameters: {
    query_by: 'title,authors',
  },
});
const searchClient = typesenseInstantsearchAdapter.searchClient;
const future = { preserveSharedStateOnUnmount: true };

export function App() {
  return (
    <div>
      <header className="header">
        <h1 className="header-title">
          <a href="/">typesense-search</a>
        </h1>
        <p className="header-subtitle">
          using{' '}
          <a href="https://github.com/algolia/instantsearch/tree/master/packages/react-instantsearch">
            React InstantSearch
          </a>
        </p>
      </header>

      <div className="container">
        <InstantSearch
          searchClient={searchClient}
          indexName="books"
          future={future}
        >
          <Configure hitsPerPage={8} />
          <div className="search-panel">
            <div className="search-panel__filters">
              <DynamicWidgets
                fallbackComponent={RefinementList}
              ></DynamicWidgets>
            </div>

            <div className="search-panel__results">
              <SearchBox placeholder="Search books…" className="searchbox" />
              <Hits hitComponent={Hit} />

              <div className="pagination">
                <Pagination />
              </div>
            </div>
          </div>
        </InstantSearch>
      </div>
    </div>
  );
}

type HitProps = {
  hit: Hit;
};

type BookHit = Hit<{
  title: string;
  authors: string[];
  publication_year?: number;
  average_rating?: number;
}>;

function Hit({ hit }: HitProps) {
  const book = hit as BookHit;
  return (
    <article className="hit">
      <h2>{book.title}</h2>
      {book.authors?.length > 0 && (
        <p className="hit-authors">{book.authors.join(', ')}</p>
      )}
      {(book.publication_year != null || book.average_rating != null) && (
        <p className="hit-meta">
          {book.publication_year != null && (
            <span>{book.publication_year}</span>
          )}
          {book.publication_year != null && book.average_rating != null && (
            <span> · </span>
          )}
          {book.average_rating != null && (
            <span>{book.average_rating.toFixed(2)} ★</span>
          )}
        </p>
      )}
    </article>
  );
}
