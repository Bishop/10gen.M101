use local

db.zips.aggregate(
    [
        { $match: { state: { $in: ['CA','NY'] } } },
        { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } },
        { $match: { pop: { $gt: 25000 } } },
        { $group: { _id: 1, pop: {$avg: "$pop"} } }
    ]
)