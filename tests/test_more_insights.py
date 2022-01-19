from src.more_insights import slice_jobs


def test_slice_jobs():
    assert slice_jobs([0, 1, 2, 3, 4, 5, 6, 7], 1, 4) == [1, 2, 3, 4]
    assert slice_jobs([0, 1, 2, 3, 4, 5], 1, 3) == [1, 2, 3]
    assert slice_jobs([0, 1, 2, 3], 1, 3) == [1, 2, 3]
    assert slice_jobs([0, 1, 2], 1, 3) == [1, 2]
    assert slice_jobs([0, 1], 1, 3) == [1]
    assert slice_jobs([0], 1, 3) == []
    assert slice_jobs([], 1, 3) == []
    assert slice_jobs([], 2, 3) == []
