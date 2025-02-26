# `markdown-dataset`

A large dataset of markdown files for testing markdown editors, parsers, renderers, and more.

_Note: This dataset is generated from the READMEs of the top starred repositories on GitHub that have an MIT license. Links to the original sources and licenses are included in the dataset._

_This repository is a fork of [davidmyersdev/markdown-dataset](https://github.com/davidmyersdev/markdown-dataset) with additional features including a Python script to convert JSON to Markdown and all the original markdown files included._

## How to use this dataset

```sh
npm install --save-dev markdown-dataset
```

```ts
import testFiles from 'markdown-dataset'

const testStrings = testFiles.reduce((decodedStrings, { markdownEncoded, markdownEncoding }) => {
  if (markdownEncoding === 'base64') {
    decodedStrings.push(atob(markdownEncoded))
  }

  return decodedStrings
}, [])
```