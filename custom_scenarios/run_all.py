#!/usr/bin/env python
"""
Runner script to execute, validate, and record all three custom NavRep scenarios:
1. Hospital Assistance Robot
2. Warehouse Navigation Robot
3. Shopping Mall Assistance Robot
"""
from __future__ import print_function
import os
import sys
import json

from custom_scenarios.hospital import hospital_scenario
from custom_scenarios.warehouse import warehouse_scenario
from custom_scenarios.shopping_mall import shopping_mall_scenario

RESULTS_FILE = "deliverables/custom_scenarios/results.json"


def main():
    print("\n" + "=" * 80)
    print("STARTING EXECUTION OF ALL CUSTOM SIMULATION SCENARIOS")
    print("=" * 80 + "\n")

    scenarios = [
        ("Hospital Assistance Robot", hospital_scenario.run),
        ("Warehouse Navigation Robot", warehouse_scenario.run),
        ("Shopping Mall Assistance Robot", shopping_mall_scenario.run),
    ]

    results = []
    passed = 0

    for name, runner in scenarios:
        print("\n>>> Launching: {} ...".format(name))
        try:
            res = runner(record=True)
            results.append(res)
            if res.get("status") == "PASS":
                passed += 1
        except Exception as e:
            print("ERROR running {}: {}".format(name, e))
            results.append({
                "scenario": name,
                "status": "FAIL",
                "error": str(e)
            })

    os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print("\n" + "=" * 80)
    print("CUSTOM SCENARIOS EXECUTION & RECORDING SUMMARY")
    print("=" * 80)
    print("{:<32} {:<8} {:<8} {:<12} {:<12} {:<8}".format(
        "Scenario Name", "Steps", "Init Dist", "Navigated", "Goal Done", "Status"
    ))
    print("-" * 80)
    for r in results:
        print("{:<32} {:<8} {:<8} {:<12} {:<12} {:<8}".format(
            r.get("scenario", "unknown"),
            r.get("steps", 0),
            r.get("initial_dist", "-"),
            r.get("dist_navigated", "-"),
            str(r.get("goal_reached", False)),
            r.get("status", "FAIL")
        ))
    print("-" * 80)
    print("SUMMARY: {}/{} CUSTOM SCENARIOS PASSED".format(passed, len(scenarios)))
    print("Results saved to:", RESULTS_FILE)


if __name__ == "__main__":
    main()
