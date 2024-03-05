from user.models import User, Room, House
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger(__name__)



def content_based_room_recommendation(user_instance):
    # Retrieve all users from the database
    all_users = list(User.objects.all())

    # Extract user attributes for content-based recommendation
    user_attributes = [
        f"{user.district} {user.city} {user.state}"
        for user in all_users
    ]

    # Debugging: Print user attributes
    logger.debug("User Attributes: %s", user_attributes)

    if not user_attributes:
        logger.warning("No user attributes found.")
        return []

    # Create TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    try:
        # Fit and transform TF-IDF matrix
        tfidf_matrix = tfidf_vectorizer.fit_transform(user_attributes)
    except ValueError as e:
        logger.error("Error during TF-IDF vectorization: %s", e)
        return []

    # Compute cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get the index of the user instance
    user_index = all_users.index(user_instance)

    # Find indices of similar users based on cosine similarity
    similar_users_indices = cosine_sim[user_index].argsort()[:-2:-1]

    # Retrieve similar users
    similar_users = [all_users[idx] for idx in similar_users_indices]

    # Extract the city of the user
    user_city = user_instance.city

    # Filter rooms based on the city of the user
    recommended_rooms = Room.objects.filter(city=user_city)

    return recommended_rooms




def content_based_house_recommendation(user_instance):
    # Retrieve all users from the database
    all_users = list(User.objects.all())

    # Extract user attributes for content-based recommendation
    user_attributes = [
        f"{user.district} {user.city} {user.state}"
        for user in all_users
    ]

    # Debugging: Print user attributes
    logger.debug("User Attributes: %s", user_attributes)

    if not user_attributes:
        logger.warning("No user attributes found.")
        return []

    # Create TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    try:
        # Fit and transform TF-IDF matrix
        tfidf_matrix = tfidf_vectorizer.fit_transform(user_attributes)
    except ValueError as e:
        logger.error("Error during TF-IDF vectorization: %s", e)
        return []

    # Compute cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get the index of the user instance
    user_index = all_users.index(user_instance)

    # Find indices of similar users based on cosine similarity
    similar_users_indices = cosine_sim[user_index].argsort()[:-2:-1]

    # Retrieve similar users
    similar_users = [all_users[idx] for idx in similar_users_indices]

    # Extract the city of the user
    user_city = user_instance.city

    # Filter houses based on the city of the user
    recommended_houses = House.objects.filter(city=user_city)

    return recommended_houses



# def content_based_house_recommendation(user_instance):
#     # Retrieve all users from the database
#     all_users = list(User.objects.all())

#     # Extract user attributes for content-based recommendation
#     user_attributes = [
#         f"{user.district} {user.city} {user.state}"
#         for user in all_users
#     ]

#     # Debugging: Print user attributes
#     logger.debug("User Attributes: %s", user_attributes)

#     if not user_attributes:
#         logger.warning("No user attributes found.")
#         return []

#     # Create TF-IDF vectorizer
#     tfidf_vectorizer = TfidfVectorizer()

#     try:
#         # Fit and transform TF-IDF matrix
#         tfidf_matrix = tfidf_vectorizer.fit_transform(user_attributes)
#     except ValueError as e:
#         logger.error("Error during TF-IDF vectorization: %s", e)
#         return []

#     # Compute cosine similarity matrix
#     cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

#     # Get the index of the user instance
#     user_index = all_users.index(user_instance)

#     # Find indices of similar users based on cosine similarity
#     similar_users_indices = cosine_sim[user_index].argsort()[:-2:-1]

#     # Retrieve similar users
#     similar_users = [all_users[idx] for idx in similar_users_indices]

#     # Extract unique city names from similar users and houses
#     similar_locations = set(user.city for user in similar_users)
#     house_locations = set(House.objects.values_list('city', flat=True))
#     all_locations = similar_locations.union(house_locations)

#     # Filter houses based on similar locations
#     recommended_houses = House.objects.filter(city__in=all_locations)

#     return recommended_houses


# utils.py

from .tim_sort import timsort


def sort_rooms_by_cost():
    # Retrieve all rooms from the database
    rooms = Room.objects.all()

    # Extract the cost of each room as the key for sorting
    room_costs = [(room.cost, room) for room in rooms]

    # Sort the room-cost tuples based on the cost using Timsort
    sorted_rooms = [room for cost, room in timsort(room_costs, key=lambda x: x[0])]


    return sorted_rooms
