# Scenario 1: Hospital Assistance Robot

## 1. Domain Overview
In clinical and healthcare facilities, autonomous service robots alleviate logistical strain by transporting pharmaceuticals, laboratory specimens, linens, and emergency medical equipment. Navigation in hospitals requires high navigational safety: corridors are narrow, doors and intersections feature blind corners, and dynamic obstacles include walking medical staff, disoriented patients, visitors, and wheeled supply carts.

## 2. Environment Configuration
- **Map Base**: ETH Zurich `asl` hospital/research floor map
- **Map Dimensions / Resolution**: 128x128 grid cells at 0.16 m/cell
- **Start Position**: `[-8.50, -9.00]` (Dispensary & Pharmacy Room)
- **Goal Position**: `[3.50, 3.50]` (Intensive Care & Inpatient Ward)
- **Euclidean Distance**: 17.0 m
- **Robot Platform**: Differential drive mobile base (0.3 m radius) equipped with 360° planar 1080-ray LiDAR sensor and forward kinematic state estimation.

## 3. Dynamic Agents & Obstacles
- **Total Dynamic Agents**: 8 pedestrians with distinct roles and crossing velocities:
  - Doctor 1: Corridor inspection traversal `[-5.0, -9.0] -> [-10.0, -9.0]`
  - Nurse 1: Hallway intersection traversal `[-8.5, -5.0] -> [-8.5, -11.0]`
  - Patient 1: Slow-moving hallway transit `[-2.0, -2.5] -> [-8.0, -2.5]`
  - Orderly 1: Medical transport cart transit `[0.0, 0.0] -> [-5.0, -5.0]`
  - Doctor 2: Patient room entrance approach `[1.0, 3.5] -> [4.5, 0.0]`
  - Visitor 1: Waiting area transit `[3.0, 1.0] -> [0.0, 3.0]`
  - Nurse 2: Secondary corridor rounds `[-6.0, -7.0] -> [-2.0, -7.0]`
  - Orderly 2: Supply transport route `[-4.0, 2.0] -> [-4.0, -2.0]`

## 4. Navigation & Obstacle Avoidance Strategy
- **Local Planner**: Dynamic Window Approach (DWA) coupled with real-time heading error feedback.
- **Safety Margin**: 0.42 m clearance envelope around static walls and moving personnel.
- **Velocity Envelope**: Linear forward velocity up to 0.70 m/s, angular velocity up to 0.80 rad/s.
- **Stall Recovery**: Automated angular realignment when linear progression drops below threshold.

## 5. Execution Instructions
```bash
./run.sh python -m custom_scenarios.hospital.hospital_scenario
```
- **Recorded Video**: `deliverables/custom_scenarios/hospital_robot.mp4`
- **Screenshot**: `deliverables/screenshots/custom_scenarios/hospital_robot.png`
