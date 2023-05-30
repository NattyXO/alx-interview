#!/usr/bin/node

const request = require('request');

// Function to retrieve the characters of a Star Wars movie
function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status:', response.statusCode);
    } else {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      // Print the characters one by one
      characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else if (response.statusCode !== 200) {
            console.error('Status:', response.statusCode);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Call the function to retrieve and print the characters
getMovieCharacters(movieId);
