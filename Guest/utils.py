from user.models import User, Room, House
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger(__name__)

def content_based_room_recommendation(user_instance):
    all_users = list(User.objects.all())

    user_attributes = [
        f"{user.district} {user.city} {user.state}"
        for user in all_users
    ]

    # Debugging: Print user attributes
    logger.debug("User Attributes: %s", user_attributes)

    if not user_attributes:
        logger.warning("No user attributes found.")
        return []

    tfidf_vectorizer = TfidfVectorizer()

    try:
        tfidf_matrix = tfidf_vectorizer.fit_transform(user_attributes)
    except ValueError as e:
        logger.error("Error during TF-IDF vectorization: %s", e)
        return []

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    user_index = all_users.index(user_instance)
    similar_users_indices = cosine_sim[user_index].argsort()[:-2:-1]
    similar_users = [all_users[idx] for idx in similar_users_indices]

    similar_locations = set(user.city for user in similar_users)
    room_locations = set(Room.objects.values_list('city', flat=True))
    all_locations = similar_locations.union(room_locations)
    recommended_rooms = Room.objects.filter(city__in=all_locations)

    return recommended_rooms

def content_based_house_recommendation(user_instance):
    all_users = list(User.objects.all())

    user_attributes = [
        f"{user.district} {user.city} {user.state}"
        for user in all_users
    ]

    # Debugging: Print user attributes
    logger.debug("User Attributes: %s", user_attributes)

    if not user_attributes:
        logger.warning("No user attributes found.")
        return []

    tfidf_vectorizer = TfidfVectorizer()

    try:
        tfidf_matrix = tfidf_vectorizer.fit_transform(user_attributes)
    except ValueError as e:
        logger.error("Error during TF-IDF vectorization: %s", e)
        return []

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    user_index = all_users.index(user_instance)
    similar_users_indices = cosine_sim[user_index].argsort()[:-2:-1]
    similar_users = [all_users[idx] for idx in similar_users_indices]

    similar_locations = set(user.city for user in similar_users)
    house_locations = set(House.objects.values_list('city', flat=True))
    all_locations = similar_locations.union(house_locations)
    recommended_houses = House.objects.filter(city__in=all_locations)

    return recommended_houses


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
