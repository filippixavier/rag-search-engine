#!/usr/bin/env python3

import argparse
import lib.keyword_search as keyword_search

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            movies = keyword_search.search_command(args.query)
            for i in range(len(movies)):
                print(f"{i + 1}. {movies[i]['title']}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()