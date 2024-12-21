#!/usr/bin/node

const fs = require('fs');

class AggregateError extends Error {
  constructor (errors) {
    super('Mulitple errors occured');
    this.errors = errors;
  }
}

const read = (file) => {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf-8', (error, data) => (error ? reject(error) : resolve(data)));
  });
};

const handleResults = (results) => {
  const errors = results
    .filter(result => result.status === 'rejected')
    .map(result => result.reason);
  if (errors.length) throw new AggregateError(errors);
  return results.map(result => result.value);
};

const promises = [process.argv[2], process.argv[3]].map(read);

const concat = async () => {
  const results = await Promise.allSettled(promises);

  try {
    const contents = handleResults(results);
    fs.writeFile(process.argv[4], contents.join(''), err => {
      if (err) throw err;
    });
  } catch (error) {
    if (!Object.keys(error).includes('errors')) {
      console.log(error);
    } else {
      for (const err of error?.errors) console.log(err);
    }
  }
};

concat();