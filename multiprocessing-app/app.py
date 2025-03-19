from flask import Flask, request, jsonify
import multiprocessing
import time
import signal

app = Flask(__name__)

processes = []

def worker(process_id):
    """Worker function that runs in a separate process."""
    while True:
        print(f"Process {process_id} is running...")
        time.sleep(2)

@app.route('/start', methods=['POST'])
def start_processes():
    global processes

    # Stop existing processes before starting new ones
    stop_processes()

    num_processes = 5  # Create 5 processes
    processes = []

    for i in range(num_processes):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    return jsonify({"message": f"Started {num_processes} processes"}), 200

@app.route('/stop', methods=['POST'])
def stop_processes():
    global processes

    for p in processes:
        p.terminate()  # Terminate each process
        p.join()

    processes = []  # Clear the process list
    return jsonify({"message": "All processes stopped"}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"running_processes": len(processes)}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
