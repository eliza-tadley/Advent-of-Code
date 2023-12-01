class Claim:
    def __init__(self, claim_id, left, top, width, height, area_covered=None):
        self.claim_id = claim_id
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.area_covered = area_covered


# Part 1
def get_visited_areas(claim):
    areas_visited = []
    for r in range(claim.height):
        for c in range(claim.width):
            point = (claim.top + r, claim.left + c)
            areas_visited.append(point)
    return areas_visited


def p1(all_claims):
    areas = set()
    overlapped_areas = set()
    for claim in all_claims:
        claim_area = get_visited_areas(claim)
        for a in claim_area:
            if a in areas:
                overlapped_areas.add(a)
            else:
                areas.add(a)
    return len(overlapped_areas)


# Part 2
def p2(all_claims):
    areas = set()
    overlapped_areas = set()
    for claim in all_claims:
        claim_area = get_visited_areas(claim)
        claim.area_covered = claim_area
        for a in claim_area:
            if a in areas:
                overlapped_areas.add(a)
            else:
                areas.add(a)
    for claim in all_claims:
        count_overlapped = 0
        for a in claim.area_covered:
            if a in overlapped_areas:
                count_overlapped += 1
        if count_overlapped == 0:
            return claim.claim_id


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    all_claims = []
    for d in data:
        claim_id = int(d.split('@')[0].replace("#", '').strip())
        after_id = d.split('@')[1]
        left = int(after_id.split(':')[0].split(',')[0].strip())
        top = int(after_id.split(':')[0].split(',')[1].strip())
        width = int(after_id.split(':')[1].split('x')[0].strip())
        height = int(after_id.split(':')[1].split('x')[1].strip())
        all_claims.append(Claim(claim_id, left, top, width, height))

    print("Part 1 Answer: {}".format(p1(all_claims)))
    print("Part 2 Answer: {}".format(p2(all_claims)))


if __name__ == "__main__":
    main()
