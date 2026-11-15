"""
Custom NavRep Environment for running user-defined scenarios with custom maps,
custom start/goal positions, and custom dynamic obstacles.
"""
import os
from pkg_resources import resource_filename
from pepper_2d_iarlenv import parse_iaenv_args, check_iaenv_args, IARLEnv
from navrep.envs.ianenv import IANEnv

class CustomNavRepEnv(IANEnv):
    def __init__(self, scenario_folder, scenario_name, map_name,
                 map_folder=None, map_downsampling_passes=1, silent=True):
        self.custom_scenario_folder = os.path.abspath(scenario_folder)
        self.custom_scenario_name = scenario_name
        self.custom_map_name = map_name
        self.custom_map_folder = (
            os.path.abspath(map_folder) if map_folder is not None
            else resource_filename('asl_pepper_2d_sim_maps', 'maps')
        )
        self.custom_map_downsampling_passes = map_downsampling_passes
        super(CustomNavRepEnv, self).__init__(silent=silent)

    def _make_env(self, silent=True, set_scenario=None):
        args = parse_iaenv_args(args=[])
        args.unmerged_scans = False
        args.continuous = True
        args.naive_plan = True
        args.no_ros = True
        args.no_pass_through = True
        args.scenario_folder = self.custom_scenario_folder
        args.scenario = self.custom_scenario_name
        args.map_folder = self.custom_map_folder
        args.map_name = self.custom_map_name
        args.map_downsampling_passes = self.custom_map_downsampling_passes
        check_iaenv_args(args)
        self.iarlenv = IARLEnv(args, silent=silent)
