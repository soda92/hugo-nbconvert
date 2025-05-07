from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from traitlets.config import Config

    c = Config()

c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags = ["hide_cell"]
c.TagRemovePreprocessor.remove_input_tags = ["hide_input"]
c.TagRemovePreprocessor.remove_all_outputs_tags = ["hide_output"]
