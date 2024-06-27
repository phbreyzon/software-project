# Song Recommender

> A music recommendation system that provides personalized song suggestions based on a user's provided songs. 

![Song Recommender Screenshot](/images/main.png)

## Installation

Alternatively you can donwload the [Appimage](https://github.com/phbreyzon/software-project/releases/download/v.1.0/MusicRecommender_v1.0.appimage) if you're on Linux

1. Clone the repository:
   
```bash
git clone https://github.com/phbreyzon/software-project.git
```

2. Install the required dependencies:
   
```bash
pip install -r requirements.txt
```

3. Ensure you have a SQLite database file named music_data.sqlite containing the necessary music data.

## Usage
The Song Recommender can be run in two ways:

1. Command-line interface: To run the Song Recommender using the command-line interface, use the following command:

```bash
python cli.py -l <liked_songs> [-n <num_recommendations>] [-f <feature_cols>]
```

- `liked_songs`: A list of song names that the user likes (required)
- `num_recommendations`: The number of song recommendations to generate (optional, default: 5)
- `feature_cols`: A list of feature columns to consider for recommendations (optional, default: predefined list)

Example:

```bash
python cli.py -l "Shape of You" "Believer" "Havana" -n 10
```

2. In order to run the GUI application, enter the following command:

```bash
python gui.py
```

## Credit 

Shoutout to [**cjy-2001**](https://github.com/cjy-2001) and his [**repository**](https://github.com/cjy-2001/song-recommender), since it provided the basis on which this project is based upon.
