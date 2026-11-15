# Scenario 2: Warehouse Navigation Robot

## 1. Domain Overview
Modern automated distribution centers rely heavily on Autonomous Mobile Robots (AMRs) to move totes, pallets, and cartons across storage aisles. The warehouse environment is characterized by tall industrial storage racks, repetitive parallel aisles, tight clearance at aisle ends, and mixed traffic including human order pickers, manual pallet jacks, and automated equipment.

## 2. Environment Configuration
- **Map Base**: `unity_scene_map` industrial logistics floor plan
- **Map Dimensions / Resolution**: 256x256 grid cells at 0.16 m/cell
- **Start Position**: `[5.00, 8.00]` (Inbound Receiving Dock & Unpacking Zone)
- **Goal Position**: `[-14.00, 3.00]` (Outbound Staging & Pallet Dispatch Dock)
- **Euclidean Distance**: 19.6 m
- **Robot Platform**: Industrial heavy-payload AMR base (0.35 m radius) equipped with 360° 1080-ray LiDAR sensor and odometry localization.

## 3. Dynamic Agents & Obstacles
- **Total Dynamic Agents**: 10 active logistics workers and transport units:
  - Picker 1: High-bay aisle replenishment `[3.0, 5.0] -> [-2.0, 5.0]`
  - Picker 2: Tote collection route `[0.0, 8.0] -> [5.0, 2.0]`
  - Forklift / Operator 1: Heavy pallet transport `[-5.0, 2.0] -> [-5.0, 8.0]`
  - Picker 3: Shelf item picking `[-8.0, 5.0] -> [-12.0, 5.0]`
  - Transporter 1: Main logistics corridor traversal `[-10.0, 1.0] -> [-3.0, 1.0]`
  - Picker 4: Storage row picking `[-12.0, 8.0] -> [-8.0, 8.0]`
  - Picker 5: Bin auditing `[2.0, 0.0] -> [-4.0, 0.0]`
  - Transporter 2: Cross-dock transit `[-6.0, -4.0] -> [-12.0, 0.0]`
  - Inventory Checker: Barcode scanning patrol `[-2.0, 7.0] -> [-2.0, 2.0]`
  - Pallet Loader: Staging dock prep `[-14.0, 7.0] -> [-10.0, 3.0]`

## 4. Navigation & Obstacle Avoidance Strategy
- **Local Planner**: C++ Dynamic Window Approach (DWA) with kinematic obstacle checking.
- **Safety Clearance**: 0.45 m protective boundary around industrial racks and personnel.
- **Velocity Envelope**: Linear forward velocity up to 0.70 m/s, rotational velocity up to 0.80 rad/s.
- **Aisle Maneuvering**: Yielding behavior when intersecting perpendicular traffic paths at shelf exits.

## 5. Execution Instructions
```bash
./run.sh python -m custom_scenarios.warehouse.warehouse_scenario
```
- **Recorded Video**: `deliverables/custom_scenarios/warehouse_robot.mp4`
- **Screenshot**: `deliverables/screenshots/custom_scenarios/warehouse_robot.png`
