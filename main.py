from typing import Callable

from UI import ui_controller
from Labs import LabsController, Lab1, Lab2, Lab3, Lab4, Lab5, Lab6, Lab7, Lab8, Lab9, Lab10, Lab11


def last_action(dict_: dict) -> Callable:
    last_index = list(dict_.keys())[-1]
    elem = dict_[last_index]
    if isinstance(elem, dict):
        return last_action(elem)

    return elem


if __name__ == '__main__':
    LabsController.add_lab('Lab1', Lab1.action)
    LabsController.add_lab('Lab2',
                           {
                               'Random Values': Lab2.random_values,
                               'Standard Noise': Lab2.action,
                               'Custom Noise': Lab2.action_custom_random,
                           })

    LabsController.add_lab('Lab3',
                           {
                               'Noise': Lab3.action,
                               'Random values': Lab3.random,
                           })
    LabsController.add_lab('Lab4 [Density & Auto correlation & Auto covariation]',
                           {
                               'Density Function': Lab4.density_function,
                               'Autocorrelation': Lab4.autocorrelation,
                               'Autocovariation': Lab4.autocovariation
                           })
    LabsController.add_lab('Lab5 [Auto Covariation]', Lab5.action)
    LabsController.add_lab('Lab6 [Shift & Spike]', Lab6.action)
    LabsController.add_lab('Lab7 [Shift & Spike Correction]',
                           {
                               'Shift correction': Lab7.action,
                               'Spikes correction': Lab7.remove_spikes
                           })
    LabsController.add_lab('Lab8 [Noise reduction]',
                           {
                               'Remove trend': Lab8.action,
                               'Remove noise (debug)': Lab8.showTrend,
                               'Sum Mean Method': Lab8.sum_mean_method,
                               'Sum Remove Noise': Lab8.sum_remove_noise
                           })

    LabsController.add_lab('Lab9 [Fourier]',
                           {
                               'Harmonic': Lab9.harm_fourier,
                               'Polyharmonic': Lab9.polyharm_fourier,
                               'Const': Lab9.const_fourier,
                               'Const Wide Window': Lab9.const_wide_window_fourier,
                               'Const Narrow Window': Lab9.const_narrow_window_fourier,
                               'Polyharm Wide Window': Lab9.polyharm_wide_window_fourier,
                               'Random': Lab9.random_spectre,
                               'Custom Random': Lab9.custom_random_spectre,
                               'Linear': Lab9.linear_spectre,
                               'Exp': Lab9.exp_spectre,
                               'Spike': Lab9.spike_spectre,
                               'File': Lab9.file_spectre,
                           })
    LabsController.add_lab('Lab10', Lab10.action)
    LabsController.add_lab('Lab11', Lab11.action)

    ui_controller.start(last_action(LabsController.actions))
