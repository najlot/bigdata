from mrjob.job import MRJob
from mrjob.step import MRStep
import csv


class MostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_find_max)
        ]

    def mapper_get_ratings(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split('\t')
        yield movie_id, 1

    def reducer_count_ratings(self, key, values):
        yield 1, (sum(values), key)

    def reducer_find_max(self, key, values):
        best_movie = max(values)
        movie_titles = csv.reader(open('u.item', encoding='ISO-8859-1'), delimiter='|')
        for movie in movie_titles:
            if int(movie[0]) == int(best_movie[1]):
                yield movie[1], best_movie[0]


if __name__ == '__main__':
    MostPopularMovie.run()
