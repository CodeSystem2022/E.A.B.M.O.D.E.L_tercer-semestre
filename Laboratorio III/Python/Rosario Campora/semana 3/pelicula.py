import os

class MovieCatalog:

    file_path = 'movies.txt'

    @classmethod
    def add_movie(cls, movie):
        with open(cls.file_path, 'a', encoding='utf8') as file:
            file.write(f'{movie.name}\n')

    @classmethod
    def list_movies(cls):
        with open(cls.file_path, 'r', encoding='utf8') as file:
            print(f'Movie Catalog'.center(50, '-'))
            print(file.read())

    @classmethod
    def delete_movies(cls):
        os.remove(cls.file_path)
        print(f'File deleted: {cls.file_path}')
