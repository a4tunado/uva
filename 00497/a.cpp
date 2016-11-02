#include <iostream>
#include <vector>
#include <string>

// https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=438

void solve(const std::vector<int> &h, std::vector<int> *r) {
    std::vector<std::vector<int> > state(h.size());

    state[0].push_back(0);
    for (int i = 1; i < h.size(); ++i) {
        int t = i;
        for (int j = 0; j < i; ++j) {
            if (h[j] < h[i] && state[j].size() > state[t].size()) { t = j; }
        }
        state[i] = state[t];
        state[i].push_back(i);
    }

    int k = 0;
    for (int i = 1; i < state.size(); ++i) {
        if (state[k].size() < state[i].size()) { k = i; }
    }

    r->swap(state[k]);
}

int main() {

    int t;
    std::string s; 
    std::vector<int> h(10000);
    std::vector<int> r(10000);

    std::getline(std::cin, s);
    t = std::stoi(s);

    std::getline(std::cin, s);
    while (t--) {
        h.clear();
        std::getline(std::cin, s);
        while (!s.empty() && !std::cin.eof()) {
            h.push_back(std::stoi(s));
            std::getline(std::cin, s);
        }
        r.clear();
        solve(h, &r);
        std::cout << "Max hits: " << r.size() << std::endl;
        for (int i = 0; i < r.size(); ++i) { std::cout << h[r[i]] << std::endl; }
        if (t) { std::cout << std::endl; }
    }

    return 0;
}
