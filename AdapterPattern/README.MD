# Adapter Pattern Example

This repository contains an example implementation of the Adapter design pattern in Python. The Adapter pattern allows incompatible interfaces to work together by creating an adapter that translates requests from one interface to another.

## Overview

In this example, we have:
- A `Target` interface that the client expects.
- An `Adaptee` class with a different interface.
- An `Adapter` class that makes the `Adaptee` compatible with the `Target`.

## Files

- `main.py`: Contains the implementation of the Adapter pattern and the client code that demonstrates its usage.

## Implementation

### Target Interface

The `Target` class defines the interface that the client expects to use.

```python
class Target:
    def request(self) -> str:
        pass
