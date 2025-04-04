# Open Navigation's Nav2 Complete Coverage Demo

## Overview

The `opennav_coverage_demo` package provides a comprehensive demonstration of the Open Navigation coverage path planning system. It showcases the integration of various components including the Coverage Navigator, Behavior Tree (BT) nodes, and Coverage Server to perform complete coverage tasks in a ROS 2 environment.

## Features

- **Complete Coverage Planning**: Demonstrates efficient area coverage path planning
- **Row-based Coverage**: Specialized implementation for row-based coverage patterns
- **Nav2 Integration**: Seamless integration with the Nav2 navigation stack
- **Behavior Tree Control**: Task execution using Behavior Trees
- **Visualization**: RViz support for monitoring coverage progress
- **Configurable**: Flexible parameters for different coverage scenarios

## Package Structure

```
opennav_coverage_demo/
├── launch/                    # Launch configurations
│   ├── bringup_launch.py     # System initialization
│   ├── coverage_demo_launch.py # Main coverage demo
│   ├── row_bringup_launch.py # Row coverage setup
│   └── row_coverage_demo_launch.py # Row coverage demo
├── params/                    # Configuration files
│   └── demo_params.yaml      # Demo parameters
├── rviz/                     # Visualization configs
├── test/                     # Test suite
├── world/                    # Simulation worlds
└── resource/                 # Additional resources
```

## Dependencies

- ROS 2 (Humble or newer)
- nav2_bringup
- opennav_coverage_msgs
- opennav_coverage_bt
- opennav_coverage
- opennav_row_coverage
- opennav_coverage_navigator
- backported_bt_navigator

## Installation

1. Clone the repository:
```bash
git clone https://github.com/opennav/opennav_coverage.git
```

2. Build the workspace:
```bash
colcon build --packages-select opennav_coverage_demo
```

## Usage

### Standard Coverage Demo

1. Source your workspace:
```bash
source install/setup.bash
```

2. Launch the demo:
```bash
ros2 launch opennav_coverage_demo coverage_demo_launch.py
```

3. Monitor the coverage progress in RViz.

### Row Coverage Demo

1. Launch the row coverage system:
```bash
ros2 launch opennav_coverage_demo row_coverage_demo_launch.py
```

2. The robot will execute a row-based coverage pattern.

## Configuration

### Parameters

The demo can be configured through `params/demo_params.yaml`. Key parameters include:
- Coverage pattern settings
- Robot dimensions
- Navigation parameters
- Behavior Tree configurations

### Launch Files

- `bringup_launch.py`: Initializes the basic system
- `coverage_demo_launch.py`: Standard coverage demonstration
- `row_bringup_launch.py`: Row coverage system setup
- `row_coverage_demo_launch.py`: Row coverage demonstration

## Visualization

The demo includes RViz configurations for monitoring:
- Coverage path planning
- Robot position and orientation
- Navigation goals
- Coverage progress
- Obstacle detection

## Testing

Run the test suite:
```bash
colcon test --packages-select opennav_coverage_demo
```

## Troubleshooting

Common issues and solutions:
1. **Launch file not found**: Ensure the package is properly built and sourced
2. **Parameter errors**: Check the YAML configuration files
3. **Visualization issues**: Verify RViz is properly configured

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This package is licensed under the Apache License 2.0.

## Maintainers

- Steve Macenski (steve@opennav.org)

## Support

For support, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue if needed

## Coverage Pattern Types

### Standard Coverage vs Row Coverage

The package supports two main types of coverage patterns, each suited for different scenarios:

#### Standard Coverage
- **Pattern**: Boustrophedon (back-and-forth) pattern
- **Best for**: 
  - Open areas without predefined paths
  - Irregularly shaped fields
  - Areas requiring complete coverage
- **Advantages**:
  - More flexible path planning
  - Better for complex geometries
  - Can handle obstacles dynamically
- **Use Cases**:
  - Lawn mowing
  - General area coverage
  - Cleaning operations
  - Search and rescue

#### Row Coverage
- **Pattern**: Parallel rows with defined spacing
- **Best for**:
  - Agricultural fields
  - Structured environments
  - Areas with predefined rows
- **Advantages**:
  - More efficient for row-based operations
  - Predictable path planning
  - Better for precision agriculture
- **Use Cases**:
  - Crop spraying
  - Seeding operations
  - Harvesting
  - Field mapping

### Key Differences

| Feature | Standard Coverage | Row Coverage |
|---------|------------------|--------------|
| Pattern Type | Boustrophedon | Parallel rows |
| Flexibility | High | Medium |
| Path Planning | Dynamic | Structured |
| Turn Efficiency | Variable | Optimized |
| Best for | Irregular areas | Structured fields |
| Implementation | `coverage_demo_launch.py` | `row_coverage_demo_launch.py` |
