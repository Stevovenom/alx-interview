#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Base URL for the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie details
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    return;
  }

  // Parse the movie data
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  // Function to fetch a character's name
  const fetchCharacter = (url, callback) => {
    request(url, (err, response, body) => {
      if (err) {
        callback(err, null);
        return;
      }
      if (response.statusCode !== 200) {
        callback(`Error: Received status code ${response.statusCode}`, null);
        return;
      }
      const characterData = JSON.parse(body);
      callback(null, characterData.name);
    });
  };

  // Fetch all characters in sequence
  const printCharacters = (index) => {
    if (index >= characters.length) {
      return;
    }
    fetchCharacter(characters[index], (err, name) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(name);
      printCharacters(index + 1);
    });
  };

  printCharacters(0);
});
