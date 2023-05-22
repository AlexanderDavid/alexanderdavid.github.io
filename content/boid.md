Title: Learning to be a Boid
Date: 2023-05-17 12:00
Category: Motion Planning
Description: Learning how to flock and generating datasets using Reynolds Boids
Status: draft

## Algorithm
The Boids algorithm is meant to simulate the movement of starling-like birds with their mesmerizing flocking behavior. While this natural behavior is certainly more complex than my simple 2D simulation there are still some really pretty emergent behaviors that fall out of such simple rules. In this way Boids are very similar to Conway's Game of Life. In the Boids simulation there are three fundimental flocking forces facilitating the behavior. 

### Seperation
The seperation force ensures no two agents get too close to eachother. The force is calculated as the sum of all the vectors pointing away from each of the neighbors. This vector is scaled by an avoidance factor which was 0.1 in my simulation. This seperation force is only applied to neighbors which fall within a protected range which was 2 in my simulation. 

```python
def seperation(self, neighbors: List[FlockingAgent]) -> None:
    close = np.zeros(2)
    for n in neighbors:
        close += self._pos - n._pos

    self._vel += close * self._avoid_factor
```

### Cohesion
The cohesion and alignment forces are strongly linked in both purpose and execution. They aim to propel both the agents position and velocity towards the average of the neighbors in the visual range. These agents are not as much of an imminent collision threat as the agents in the protected range and this is what the real flocking behavior emerges from.

```python
def cohesion(self, neighbors: List[FlockingAgent]) -> None:
    avg_pos = np.zeros(2)

    for n in neighbors:
        avg_pos += n._pos
    avg_pos /= max(len(neighbors), 1)

    self._vel += (avg_pos - self._pos) * self._center_factor
```

### Alignment

```python
def alignment(self, neighbors: List[FlockingAgent]) -> None:
    avg_vel = np.zeros(2)

    for n in neighbors:
        avg_vel += n._vel
    avg_vel /= max(len(neighbors), 1)

    self._vel += (avg_vel - self._vel) * self._match_factor
```

## Learning to Flock
Over the last several years there 
[@durve2020learning] [@perrin2021flock]
## Generated Data