import socket
import threading
import time
from datetime import datetime, timedelta


def slave_node(port, initial_time_offset):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(1)
    print(f"Slave with initial time offset of {initial_time_offset} seconds listening on port {port}")

    while True:
        conn, addr = server.accept()
        with conn:
            data = conn.recv(1024)
            if data:
                if data.decode('utf-8') == 'TIME':
                    # Dynamically calculate skewed_time based on the current time and the initial offset
                    skewed_time = datetime.now() + timedelta(seconds=initial_time_offset)
                    conn.sendall(str(skewed_time.timestamp()).encode('utf-8'))
                elif data.startswith(b'ADJUST'):
                    adjustment = float(data.decode('utf-8').split()[1])
                    # Apply the adjustment to the initial_time_offset
                    initial_time_offset += adjustment
                    print(f"Received adjustment of {adjustment} seconds. New offset: {initial_time_offset} seconds.")


def master_node(slave_ports):
    while True:
        time_differences = []
        master_current_time = datetime.now()

        # Collect current times from all slaves and calculate their differences from the master's time
        for port in slave_ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(('localhost', port))
                sock.sendall(b'TIME')
                response = sock.recv(1024)
                slave_time = datetime.fromtimestamp(float(response.decode('utf-8')))
                time_diff = (slave_time - master_current_time).total_seconds()
                time_differences.append(time_diff)

        if time_differences:
            average_diff = sum(time_differences) / len(time_differences)
        else:
            average_diff = 0

        # Dispatch the adjustment to each slave node
        for port in slave_ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(('localhost', port))
                adjustment_msg = f'ADJUST {-average_diff}'.encode('utf-8')
                sock.sendall(adjustment_msg)

        print(f"Dispatched adjustment of {-average_diff} seconds to all slaves.\n")
        time.sleep(30)  # Sync every 30 seconds


if __name__ == "__main__":
    slave_ports = [8000, 8001, 8002]  # Slave ports
    time_offsets = [5, -5, 10]  # Initial time offsets for each slave

    # Start slave nodes
    for port, offset in zip(slave_ports, time_offsets):
        threading.Thread(target=slave_node, args=(port, offset)).start()

    time.sleep(1)  # Ensure slaves are up
    master_node(slave_ports)  # Start master node
