from logger_setup import setup_logger

logger = setup_logger()

def run_tests():
    test_inputs = [f"test_input_{i}" for i in range(1, 21)]

    for idx, input_str in enumerate(test_inputs, start=1):
        logger.info(f"Running Test {idx} with input: {input_str}")

        try:
            output_dict = my_function(input_str)

            # Summary
            logger.info(f"Test {idx} completed successfully. Keys returned: {list(output_dict.keys())}")

            # Full detail (only if LOG_LEVEL=2)
            logger.debug(f"Test {idx} output: {output_dict}")

        except Exception as e:
            logger.error(f"Test {idx} failed with input={input_str}, error={e}", exc_info=True)


if __name__ == "__main__":
    run_tests()