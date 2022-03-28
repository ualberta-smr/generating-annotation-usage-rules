from typing import List

# both are useful for future plans
DEFAULT_USER_ID = 0
DEFAULT_PACKAGE_ID = 1

class RuleLabels:
    CORRECT = "correct"
    INCORRECT = "not_a_rule"
    UNLABELED = "unlabeled"

    def label_is_supported(label: str) -> bool:
        return label in {RuleLabels.CORRECT, RuleLabels.INCORRECT}

    def assert_label_is_supported(label: str) -> bool:
        assert label in {RuleLabels.CORRECT, RuleLabels.INCORRECT}, \
            f"Label '{label}' is not supported, it needs to be one of ['correct', 'not_a_rule']"
    
    def get_all() -> List[str]:
        return [RuleLabels.CORRECT, RuleLabels.INCORRECT, RuleLabels.UNLABELED]