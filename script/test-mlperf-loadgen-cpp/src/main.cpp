/* Developer(s): Grigori Fursin */

#include <iostream>

#include "common.h"

#include "loadgen.h"
#include "test_settings.h"

class InputSettings {

public:
    InputSettings() {
        mlperf_conf_path = getenv("CM_MLPERF_CONF", "../inference/mlperf.conf");
        user_conf_path = getenv("CM_MLPERF_USER_CONF", "../inference/vision/classification_and_detection/user.conf");
        audit_conf_path = getenv("CM_MLPERF_INFERENCE_AUDIT_PATH", "");
        output_dir = getenv("CM_MLPERF_OUTPUT_DIR", ".");
        backend_name = getenv("CM_MLPERF_BACKEND", "onnxruntime");
        device_name = getenv("CM_MLPERF_DEVICE", "cpu");
        model_name = getenv("CM_MODEL", "resnet50");
        model_path = getenv("CM_ML_MODEL_FILE_WITH_PATH", "");
        dataset_preprocessed_path = getenv("CM_DATASET_PREPROCESSED_PATH", "");
        dataset_path = getenv("CM_DATASET_PATH", "");
        dataset_list = getenv("CM_DATASET_LIST", "");
        imagenet_val_path = getenv("CM_DATASET_AUX_PATH", "") + "/val.txt";
        scenario_name = getenv("CM_MLPERF_LOADGEN_SCENARIO", "Offline");

        mode_name = getenv("CM_MLPERF_LOADGEN_MODE", "PerformanceOnly");
        if (mode_name == "accuracy")
            mode_name = "AccuracyOnly";
        if (mode_name == "performance")
            mode_name = "PerformanceOnly";

        query_count_override = std::stol(getenv("CM_MLPERF_LOADGEN_QUERY_COUNT", "0"));
        query_count_override = 0;
        performance_sample_count = std::stol(getenv("CM_MLPERF_LOADGEN_PERFORMANCE_SAMPLE_COUNT", "0"));
        batch_size = std::stol(getenv("CM_MLPERF_LOADGEN_MAX_BATCHSIZE", "32"));

        std::cout << "MLPerf Conf path: " << mlperf_conf_path << std::endl;
        std::cout << "User Conf path: " << user_conf_path << std::endl;
        std::cout << "Dataset Preprocessed path: " << dataset_preprocessed_path << std::endl;
        std::cout << "Dataset List filepath: " << dataset_list << std::endl;
        std::cout << "Scenario: " << scenario_name << std::endl;
        std::cout << "Mode: " << mode_name << std::endl;
        std::cout << "Batch size: " << batch_size << std::endl;
        std::cout << "Query count override: " << query_count_override << std::endl;
        std::cout << "Performance sample count override in application: " << performance_sample_count << std::endl;
    }

    std::string mlperf_conf_path;
    std::string user_conf_path;
    std::string audit_conf_path;
    std::string output_dir;
    std::string backend_name;
    std::string device_name;
    std::string model_name;
    std::string model_path;
    std::string dataset_preprocessed_path;
    std::string dataset_path;
    std::string dataset_list;
    std::string imagenet_val_path;
    std::string scenario_name;
    std::string mode_name;
    size_t performance_sample_count;
    size_t batch_size;
    size_t query_count_override;
};

int main(int argc, const char *argv[]) {
    // configure test settings
    std::cout << "========================================================" << std::endl;

    std::cout << "- Initializing MLPerf input settings" << std::endl;
    std::cout << std::endl;
    InputSettings input_settings;
    std::cout << std::endl;
    std::cout << "  SUCCESS!" << std::endl;

    std::cout << "- Initializing MLPerf" << std::endl;
    mlperf::TestSettings test_settings;
    std::cout << "  SUCCESS!" << std::endl;

    std::cout << "========================================================" << std::endl;
}
