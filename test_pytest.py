from voc_utils.voc_utils import PascalVOCDataset
import os

DIR_VOC_ROOT = os.environ["DIR_VOC_ROOT"]
DIR_PASCAL_CSV = os.environ["DIR_PASCAL_CSV"]


def test_part_dataset():
    for image_set in PascalVOCDataset.list_image_sets():
        for split in PascalVOCDataset.SPLITS():
            dset = PascalVOCDataset(DIR_VOC_ROOT, DIR_PASCAL_CSV)
