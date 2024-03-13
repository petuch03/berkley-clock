# Berkeley Clock Synchronization Algorithm Implementation

The implementation simulates a master-slave architecture to synchronize time across multiple nodes using Python. Below are the key aspects of the implementation, including motivation, details, and instructions for running the simulation.

## Programming Language Choice
- Python: Chosen for its simplicity, extensive standard library, and robust support for networking.

## Implementation Details

This implementation simulates network communication within a single machine using distinct port numbers for each node. It uses Python's `socket` library for network communication, alongside `datetime` and `threading` libraries for handling time and concurrency.

### Master Node

- Functionality: The master node periodically requests the current times from all slave nodes. It then calculates the average time offset by excluding its own time to ensure that the synchronization is based on the consensus among the slave nodes rather than aligning strictly with the master's clock.
- Objective: Dispatches an adjustment message to each slave, dictating the necessary clock adjustment to minimize the time difference across the network.

### Slave Node

- Responsiveness: Each slave node responds to the master's request by sending their current time.
- Adjustment Compliance: Adjusts their clocks according to the master's adjustment directive, aiming for closer alignment with the network-wide consensus time.

### Network Communication

- Utilizing Python's `socket` library, the implementation facilitates communication between nodes, demonstrating how distributed systems can synchronize time over a network.
- TCP/IP Sockets: Chosen for their reliability in order to ensure that time synchronization messages are accurately delivered and processed. This choice is crucial for maintaining the integrity of the synchronization process, considering the need for precise and reliable message exchanges in clock synchronization.
- Single Machine Simulation: For simplicity, the network is simulated within a single machine (`localhost`), using distinct port numbers for each node's communication. This approach simplifies the demonstration of the Berkeley Algorithm's principles without the complexities of a real network environment.

## Code Structure

```plaintext
- slave_node(port, initial_time_offset): Initializes a slave node with a specific port and simulated initial time offset.
- master_node(slave_ports): The master node that coordinates time synchronization among slave nodes.
- main: Entry point that starts slave nodes on different ports and then the master node to synchronize their clocks.
```

## Running the Simulation

To run the simulation, ensure Python 3.x is installed on your machine. Navigate to the project directory, and run:

```bash
python3 main.py
```

This will start the simulation with predefined slave nodes and time offsets. Adjust `slave_ports` and `time_offsets` in the `__main__` section as needed to simulate different scenarios.

## Output sample

```
Slave with initial time offset of 10 seconds listening on port 8002
Slave with initial time offset of -5 seconds listening on port 8001
Slave with initial time offset of 5 seconds listening on port 8000
Received adjustment of -3.347477 seconds. New offset: 1.652523 seconds.
Received adjustment of -3.347477 seconds. New offset: -8.347477 seconds.
Received adjustment of -3.347477 seconds. New offset: 6.652523 seconds.
Dispatched adjustment of -3.347477 seconds to all slaves.

Received adjustment of 0.006145333333333447 seconds. New offset: 1.6586683333333334 seconds.
Received adjustment of 0.006145333333333447 seconds. New offset: -8.341331666666665 seconds.
Received adjustment of 0.006145333333333447 seconds. New offset: 6.658668333333334 seconds.
Dispatched adjustment of 0.006145333333333447 seconds to all slaves.

Received adjustment of 0.00035733333333295053 seconds. New offset: 1.6590256666666663 seconds.
Received adjustment of 0.00035733333333295053 seconds. New offset: -8.340974333333332 seconds.
Received adjustment of 0.00035733333333295053 seconds. New offset: 6.6590256666666665 seconds.
Dispatched adjustment of 0.00035733333333295053 seconds to all slaves.

Received adjustment of -0.036717999999999584 seconds. New offset: 1.6223076666666667 seconds.
Received adjustment of -0.036717999999999584 seconds. New offset: -8.377692333333332 seconds.
Received adjustment of -0.036717999999999584 seconds. New offset: 6.622307666666667 seconds.
Dispatched adjustment of -0.036717999999999584 seconds to all slaves.

Received adjustment of 0.037814999999999856 seconds. New offset: 1.6601226666666666 seconds.
Received adjustment of 0.037814999999999856 seconds. New offset: -8.339877333333332 seconds.
Received adjustment of 0.037814999999999856 seconds. New offset: 6.660122666666667 seconds.
Dispatched adjustment of 0.037814999999999856 seconds to all slaves.

Received adjustment of -0.0004946666666665323 seconds. New offset: 1.659628 seconds.
Received adjustment of -0.0004946666666665323 seconds. New offset: -8.340371999999999 seconds.
Received adjustment of -0.0004946666666665323 seconds. New offset: 6.6596280000000005 seconds.
Dispatched adjustment of -0.0004946666666665323 seconds to all slaves.

Received adjustment of -0.023874000000000173 seconds. New offset: 1.635754 seconds.
Received adjustment of -0.023874000000000173 seconds. New offset: -8.364245999999998 seconds.
Received adjustment of -0.023874000000000173 seconds. New offset: 6.635754 seconds.
Dispatched adjustment of -0.023874000000000173 seconds to all slaves.

Received adjustment of 0.0228233333333329 seconds. New offset: 1.658577333333333 seconds.
Received adjustment of 0.0228233333333329 seconds. New offset: -8.341422666666665 seconds.
Received adjustment of 0.0228233333333329 seconds. New offset: 6.658577333333334 seconds.
Dispatched adjustment of 0.0228233333333329 seconds to all slaves.

Received adjustment of -5.03333333332634e-05 seconds. New offset: 1.6585269999999996 seconds.
Received adjustment of -5.03333333332634e-05 seconds. New offset: -8.341472999999997 seconds.
Received adjustment of -5.03333333332634e-05 seconds. New offset: 6.658527 seconds.
Dispatched adjustment of -5.03333333332634e-05 seconds to all slaves.

Received adjustment of 0.0011303333333335293 seconds. New offset: 1.659657333333333 seconds.
Received adjustment of 0.0011303333333335293 seconds. New offset: -8.340342666666663 seconds.
Received adjustment of 0.0011303333333335293 seconds. New offset: 6.6596573333333335 seconds.
Dispatched adjustment of 0.0011303333333335293 seconds to all slaves.
```


