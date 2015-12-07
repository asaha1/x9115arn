# This model has been generated from the quality assurance part of integrated project model
# The aim of the model is to reduce the value of the stocks detected errors and escaped errors

import IPM.Utility
import random

'''
aux_list
0 = software development rate
1 = average qa delay
2 = potentially detectable errors
3 = DSI per task
4 = multiplier for losses
5 = percent of job actually worked
6 = daily MP for QA
7 = percent of job actually worked
8 = DSI per task
9 = schedule pressure
10 = ratio of pros to rookies
11 = software development rate
12 = qa rate
13 = average # errors per task
14 = daily mp for rework
15 = multiplier for losses
16 = error generation rate
'''


def integrated_project_model_qa(aux_list):
    # flows and auxilliaries and stocks
    # left part
    sd_rate_F = aux_list[0]
    qa_rate_A = max(aux_list[0] - aux_list[1], 0)
    qa_rate_F = qa_rate_A

    tasks_worked_S = max(sd_rate_F - qa_rate_F, 0)
    if tasks_worked_S == 0:
        average_errors_per_task_A = 0
    else:
        average_errors_per_task_A = max(aux_list[2] / tasks_worked_S, 0)
    error_density_A = average_errors_per_task_A * (1000 / aux_list[3])
    multiplier_due_to_error_density_A = error_density_A

    # middle part
    nominal_qa_manpower_needed_per_error_A = aux_list[5]
    qa_manpower_needed_to_detect_an_error_A = nominal_qa_manpower_needed_per_error_A * (
        1 / aux_list[4]) * multiplier_due_to_error_density_A

    potential_error_detection_rate_A = aux_list[6] / qa_manpower_needed_to_detect_an_error_A

    # top part
    nominal_errors_committed_per_dsi_A = aux_list[7]
    nominal_errors_committed_per_task_A = nominal_errors_committed_per_dsi_A * aux_list[8] / 1000

    multiplier_due_to_schedule_pressure_A = aux_list[9]
    multiplier_due_to_workforce_mix_A = aux_list[10]
    error_generation_rate_F = aux_list[
                                  11] * nominal_errors_committed_per_task_A * multiplier_due_to_schedule_pressure_A * multiplier_due_to_workforce_mix_A

    # central part
    error_escape_rate_F = aux_list[12] * aux_list[13]
    potentially_detectable_errors_S = max(error_generation_rate_F - error_escape_rate_F, 0)
    error_detection_rate_F = max(potential_error_detection_rate_A, potentially_detectable_errors_S)

    nominal_rework_manpower_needed_per_error_A = aux_list[5]

    detected_errors_S = error_detection_rate_F
    actual_rework_manpower_needed_per_error_A = nominal_rework_manpower_needed_per_error_A / aux_list[15]
    rework_rate_F = aux_list[14] / aux_list[15]

    # bottom part
    reworked_errors_during_devel_S = rework_rate_F

    # bottom right part
    escaped_errors_S = error_escape_rate_F
    count_detected_errors_F = error_detection_rate_F
    cumulative_detected_errors = count_detected_errors_F

    generation_rate_F = aux_list[16]
    cumulative_errors_S = generation_rate_F
    percent_errors_detected_A = 100 * cumulative_detected_errors / (cumulative_errors_S + 0.001)

    return detected_errors_S, escaped_errors_S


if __name__ == "__main__":
    list = [random.uniform(low, high) for low, high in IPM.Utility.bounds]
    # print list
    print integrated_project_model_qa(list)
