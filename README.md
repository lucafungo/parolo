# Parolo

Parolo is a word guessing game  ispired by [Wordle](https://www.nytimes.com/games/wordle/index.html) that challenges the user to guess a randomly selected five-letter word. The user has six attempts to correctly guess the word, and is provided with feedback on their guesses. The game uses `Python 3` and the `colorama` package to enable colored text in the terminal.

## Getting started
To get started, clone the repository and navigate to the project directory.
bash


```bash
git clone https://github.com/lucafungo/parolo.git
```

## Docker
To build a Docker image of the game, use the following command in your terminal:

```bash
docker build -t parolo .
```
To run the game in a Docker container, use the following command:

```
docker run -it word_guessing_game
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact

If you have any questions or comments, please feel free to contact the author at luca.alfieri@xandertalent.com.
