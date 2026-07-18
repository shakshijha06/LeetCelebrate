#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        unordered_set<int> seen;

        for (int x : nums) {
            if (seen.find(x) != seen.end()) {
                return true;
            }

            seen.insert(x);
        }

        return false;
    }
};