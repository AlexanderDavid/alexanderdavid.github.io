Title: Learning to be a Boid
Date: 2023-05-17 12:00
Category: Motion Planning
Description: Learning how to flock and generating datasets using Reynolds Boids

## Algorithm
The Boids algorithm is meant to simulate the movement of starling-like birds with their
mesmerizing flocking behavior. While this natural behavior is certainly more complex than
my simple 2D simulation there are still some really pretty emergent behaviors that fall out
of such simple rules. In this way Boids are very similar to Conway's Game of Life. 

### Seperation

```python
def __seperation(self, neighbors: List["BoidAgent"]) -> None:
    close = np.zeros(2)
    for n in neighbors:
        close += self._pos - n._pos

    self._vel += close * self._avoid_factor
```

$\alpha$

### Cohesion
### Alignment

## Simulation

## Generated Data