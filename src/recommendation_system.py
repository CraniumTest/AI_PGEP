import numpy as np
import pandas as pd

def recommend_activities(guest_id, guest_data, activity_matrix):
    guest_preferences = guest_data.loc[guest_id, 'activities']
    preference_vector = np.array([int(pref) for pref in guest_preferences.split(',')])
    
    # Compute similarity
    similarities = np.dot(activity_matrix, preference_vector)
    recommendations = np.argsort(similarities)[-5:] # Top 5 recommendations
    return recommendations

# Dummy data setup
guest_data = pd.DataFrame({'activities': ['1,0,1', '1,1,0', '0,1,1']})
activity_matrix = np.array([[1, 0, 1], [1, 1, 0], [0, 1, 1]])

recommend_activities(0, guest_data, activity_matrix)
