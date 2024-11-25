import arrow


def test_dst():
    # 1667725199 11/6/2022 1:59:59AM GMT-7 DST
    # 1667725200 11/6/2022 1:00:00AM GMT-8
    before_dst = arrow.get(1667725199, tzinfo="America/Los_Angeles")
    print(before_dst)
    after_dst = arrow.get(1667725200, tzinfo="America/Los_Angeles")
    print(after_dst)
    secs = (after_dst - before_dst).total_seconds()
    print(secs)


test_dst()
