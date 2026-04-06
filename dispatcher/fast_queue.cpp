#include <iostream>
#include <queue>
#include <string>
#include <thread>
#include <chrono>

using namespace std;

// ==========================================
// QRT C++ HIGH-SPEED DISPATCH ENGINE
// ==========================================

// Define the structure of an Alert Task
struct AlertTask {
    string ip_address;
    string payload;
};

class AlertDispatcher {
private:
    queue<AlertTask> dispatch_queue;

public:
    // Add targets to the queue at high speed
    void enqueue_target(string ip, string message) {
        AlertTask newTask = {ip, message};
        dispatch_queue.push(newTask);
        cout << "[QUEUE] Target " << ip << " added to dispatch queue. (Queue size: " << dispatch_queue.size() << ")" << endl;
    }

    // Process the queue and "fire" the alerts
    void fire_alerts() {
        cout << "\n[DISPATCH] Initiating high-speed alert broadcast..." << endl;
        
        while (!dispatch_queue.empty()) {
            AlertTask currentTask = dispatch_queue.front();
            
            // Simulate network transmission time (microseconds in reality, milliseconds here for the prototype)
            this_thread::sleep_for(chrono::milliseconds(150)); 
            
            cout << "  => [SENT] CRITICAL ALERT delivered to IP: " << currentTask.ip_address << endl;
            
            // Remove from queue after sending
            dispatch_queue.pop(); 
        }
        
        cout << "\n[SYSTEM] Broadcast Complete. All targets in danger zone notified." << endl;
    }
};

int main() {
    cout << "======================================" << endl;
    cout << "  QRT DISPATCHER ENGINE INITIALIZED" << endl;
    cout << "======================================" << endl;

    AlertDispatcher qrt_dispatcher;
    string crisis_message = "CRITICAL ALERT: Seek shelter immediately. QRT Protocol Active.";

    // Simulating the hand-off from your Python script
    cout << "\n[LINK] Receiving target list from Python AI Engine..." << endl;
    
    // The exact IPs your Python script just found
    qrt_dispatcher.enqueue_target("192.168.1.10", crisis_message);
    qrt_dispatcher.enqueue_target("10.0.0.5", crisis_message);

    // Fire the alerts
    qrt_dispatcher.fire_alerts();

    return 0;
}