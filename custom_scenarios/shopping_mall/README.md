# Scenario 3: Shopping Mall Assistance Robot

## 1. Domain Overview
In retail and commercial complexes, social mobile robots assist visitors with wayfinding, directory queries, and customer escorting. A commercial shopping concourse presents complex social navigation challenges: highly dynamic, uncoordinated pedestrian movement, walking family groups, sudden stops in front of retail kiosks, meandering trajectories, and structural pillars.

## 2. Environment Configuration
- **Map Base**: `asl_office_j` expansive concourse and retail corridor map
- **Map Dimensions / Resolution**: 512x512 grid cells at 0.16 m/cell
- **Start Position**: `[-4.00, -1.50]` (Mall Entrance / Central Atrium Information Desk)
- **Goal Position**: `[5.50, -0.50]` (Anchor Department Store & Retail Promenade)
- **Euclidean Distance**: 9.55 m
- **Robot Platform**: Service & escort robot (0.30 m radius) equipped with 360° 1080-ray LiDAR sensor and orientation tracking.

## 3. Dynamic Agents & Obstacles
- **Total Dynamic Agents**: 14 dynamic shoppers, groups, and children:
  - Shopper Group 1 (Pair): Entering concourse `[-18.0, -3.0] -> [-22.0, -3.0]` & `[-18.0, -4.0] -> [-22.0, -4.0]`
  - Shopper 3: Crossing from storefront to food court `[-14.0, -3.5] -> [-18.0, 1.0]`
  - Window Shopper: Strolling along display windows `[-10.0, -1.0] -> [-5.0, -1.0]`
  - Shopper Group 2 (Pair): Walking together towards exit `[-5.0, -3.0] -> [-10.0, -3.0]` & `[-5.0, -4.0] -> [-10.0, -4.0]`
  - Family Group (Pair): Meandering across central plaza `[0.0, -2.0] -> [-4.0, 2.0]` & `[1.0, -2.0] -> [-4.0, 3.0]`
  - Shopper 8: Direct crossing `[4.0, 0.0] -> [0.0, 0.0]`
  - Shopper 9: Corridor transition `[6.0, 3.0] -> [2.0, 1.0]`
  - Shopper 10: Store egress `[8.0, 5.0] -> [4.0, 5.0]`
  - Shopper 11: Approaching information desk `[10.0, 2.0] -> [12.0, 5.0]`
  - Store Clerk: Retail staff patrol `[11.0, 6.0] -> [8.0, 6.0]`
  - Child Runner: Rapid crossing trajectory `[-12.0, -3.0] -> [-6.0, -3.0]`

## 4. Navigation & Obstacle Avoidance Strategy
- **Local Planner**: C++ Dynamic Window Approach (DWA) with dense crowd penalty.
- **Safety Clearance**: 0.45 m social boundary around moving pedestrians and structural columns.
- **Velocity Envelope**: Linear forward velocity up to 0.70 m/s, rotational velocity up to 0.80 rad/s.
- **Social Navigation**: Yielding to approaching groups while maintaining directional progress along the primary concourse axis.

## 5. Execution Instructions
```bash
./run.sh python -m custom_scenarios.shopping_mall.shopping_mall_scenario
```
- **Recorded Video**: `deliverables/custom_scenarios/shopping_mall_robot.mp4`
- **Screenshot**: `deliverables/screenshots/custom_scenarios/shopping_mall_robot.png`
