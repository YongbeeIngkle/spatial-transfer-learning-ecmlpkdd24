from data_process.split import LimaSplitLdfInputCompose

if __name__ == "__main__":
    target_train_number = 6 ## 6
    source_type = "whole" ## other source data options -- "west", "east-north"
    ldf_a = False
    number_of_splits = 3
    station_num = 12

    split_compose = LimaSplitLdfInputCompose(target_train_number, station_num, ldf_a)
    split_compose.save(number_of_splits, source_type)
