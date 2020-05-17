import os
import sys
from zipfile import ZipFile

import requests
from typing import List

from flair.data import Sentence, Label
from flair.models import TextClassifier


class SentimentTagger:
    def __init__(self):

        classifier_path = os.path.join(*os.path.split(os.path.abspath(__file__))[:-1], os.path.join('cache', 'sentiment', 'best-model.pt'))
        print(os.path.split(os.path.abspath(__file__)))
        print(classifier_path)
        download_model_if_not_exists('sentiment', classifier_path)
        self.classifier: TextClassifier = TextClassifier.load(classifier_path)

    def predict(self, tweet_text_list: List[str]) -> List[Label]:
        sentences = [Sentence(t) for t in tweet_text_list]

        self.classifier.predict(sentences)
        return [sentence.labels[0] for sentence in sentences]


class PoliticalViewsTagger:
    def __init__(self):

        classifier_path = os.path.join(*os.path.split(os.path.abspath(__file__))[:-1], os.path.join('cache', 'sentiment', 'best-model.pt'))
        download_model_if_not_exists('political_views', classifier_path)
        self.classifier: TextClassifier = TextClassifier.load(classifier_path)

    def predict(self, tweet_text_list: List[str]) -> List[Label]:
        sentences = [Sentence(t) for t in tweet_text_list]

        self.classifier.predict(sentences)
        return [sentence.labels[0] for sentence in sentences]


def download_model_if_not_exists(model_type, path):

    try:
        os.makedirs(os.path.split(path)[0])
    except FileExistsError:
        pass

    if model_type == 'sentiment':
        url = 'https://github.com/piotrgajdzica/sentiment-analysis/releases/download/1.0/sentiment.zip'
    elif model_type == 'political_views':
        url = 'https://github.com/piotrgajdzica/sentiment-analysis/releases/download/1.0/political_views.zip'
    else:
        raise Exception('Wrong model type')

    if not os.path.isfile(path):
        zip_path = path.replace('.pt', '.zip')

        # r = requests.get(url, allow_redirects=True)
        # open(zip_path, 'wb').write(r.content)

        with open(zip_path, "wb") as f:
            print("Downloading %s to cache" % url)
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()
        ZipFile(zip_path).extractall(path=os.path.split(zip_path)[0])


if __name__ == '__main__':
    SentimentTagger().predict([''])
