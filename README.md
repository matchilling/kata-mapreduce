# MapReduce Kata

A code kata is an exercise in programming which helps a programmer hone their skills through practice and repetition. The term was probably first coined by Dave Thomas, co-author of the book "The Pragmatic Programmer", in a bow to the Japanese concept of kata in the martial arts.

## Basic setup & usage

The project uses Docker and GNU make for running mapreduce jobs on AWS EMR. To get started execute the following steps in our terminal.

```bash
# 1.1 Create an .env file in the project root (c.f. .env.dist)
# 1.2 Create an mrjob.conf file in the project root (c.f. mrjob.conf.dist)
# 1.3 Build the project image from the Dockerfile
$ make build

# 2.1 Run bash interactively in a the container
$ make shell
```

Check the self-documented [makefile](./makefile) for further details.

## Bigram

[MRBigram.py](./bin/MRBigram.py) calculates the conditional probability that a word occurs immediately after the word "my" using the entire collection of over 200,000 short jokes ([from Kaggle](https://www.kaggle.com/abhinavmoudgil95/short-jokes)).

Which 10 words are most likely to be said immediately after the word "my", i.e. with the highest conditional probability?

```bash
# Run MRBigram with a small dataset
$ make shell
$ ./bin/MRBigram.py data/shortjokes_small.csv

# Run MRBigram on AWS EMR with the complete dataset
$ make shell
$ ./bin/MRBigram.py data/shortjokes_complete.csv -r emr -c mrjob.conf

# Download the output from s3
$ cat output/MRBigram/result | sort -r | head -n 10
# 5.5085675287006115 "wife"
# 4.0071172642406220 "girlfriend"
# 2.9517147244497526 "friend"
# 1.7476296097691764 "women"
# 1.6208838082238526 "dad"
# 1.2723328539742120 "coffee"
# 1.2162722109830110 "life"
# 1.2089599532015503 "favorite"
# 1.1212128598240183 "mom"
# 1.1041509250006094 "son"
```

## License

This distribution is covered by the **GNU GENERAL PUBLIC LICENSE**, Version 3, 29 June 2007.

## Support & Contact

Having trouble with this repository? Check out the documentation at the repository's site or contact m@matchilling.com and we’ll help you sort it out.

Happy Coding

:v:
