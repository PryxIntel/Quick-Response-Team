import numpy as np
from sklearn.linear_model import LogisticRegression
import math

# ==========================================
# MODULE 1: AI THREAT VERIFICATION
# ==========================================

def train_threat_model():
    print("[SYSTEM] Training QRT Threat Verification Model...")
    # Features: [Source Credibility (1-10), Keyword Urgency (1-10), Sensor Anomaly Level (1-10)]
    X_train = np.array([
        [2, 3, 1],  # Low credibility, low urgency -> False Alarm
        [9, 2, 2],  # High credibility, but low urgency -> Normal News
        [8, 9, 8],  # High credibility, high urgency, high sensors -> CRISIS
        [1, 9, 2],  # Low credibility, high urgency -> Fake News/Prank
        [10, 10, 9] # Max credibility, max urgency -> SEVERE CRISIS
    ])
    
    # Labels: 0 = Ignore, 1 = Trigger Alert
    y_train = np.array([0, 0, 1, 0, 1])
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

# ==========================================
# MODULE 2: PRECISION GEO-TARGETING
# ==========================================

# Mock database of connected users (IP Address, Latitude, Longitude)
active_users = [
    {"ip": "192.168.1.10", "lat": 26.7606, "lon": 83.3732}, # User in Zone A
    {"ip": "10.0.0.5",     "lat": 26.7610, "lon": 83.3740}, # User in Zone A
    {"ip": "172.16.0.8",   "lat": 28.6139, "lon": 77.2090}, # User far away (Zone B)
]

def calculate_distance(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate distance between two points on Earth
    R = 6371.0 # Radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def find_users_in_danger_zone(crisis_lat, crisis_lon, radius_km):
    print(f"\n[SCAN] Scanning for users within {radius_km}km of [{crisis_lat}, {crisis_lon}]...")
    targeted_ips = []
    
    for user in active_users:
        distance = calculate_distance(crisis_lat, crisis_lon, user["lat"], user["lon"])
        if distance <= radius_km:
            targeted_ips.append(user["ip"])
            print(f"  -> TARGET LOCKED: IP {user['ip']} (Distance: {distance:.2f}km)")
            
    return targeted_ips

# ==========================================
# MAIN EXECUTION: SIMULATING A CRISIS
# ==========================================

if __name__ == "__main__":
    # 1. Boot up the AI
    threat_model = train_threat_model()
    
    # 2. Simulate an incoming alert signal (e.g., from a weather agency)
    # Incoming data: Credibility=9, Urgency=9, Sensors=8
    incoming_signal = np.array([[9, 9, 8]]) 
    
    print("\n[ALERT] Incoming signal detected. Analyzing...")
    is_crisis = threat_model.predict(incoming_signal)[0]
    
    if is_crisis == 1:
        print("[CRITICAL] Signal Verified as Legitimate Threat.")
        
        # 3. Define the blast radius/danger zone (e.g., coordinates for Gorakhpur region)
        crisis_latitude = 26.7600
        crisis_longitude = 83.3700
        danger_radius_km = 5.0 
        
        # 4. Geofence and target
        targets = find_users_in_danger_zone(crisis_latitude, crisis_longitude, danger_radius_km)
        
        print(f"\n[DISPATCH] Pushing {len(targets)} target IPs to the C++ High-Speed Queue.")
    else:
        print("[SAFE] Signal classified as noise or false alarm. No action taken.")