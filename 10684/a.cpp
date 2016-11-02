#include <iostream>
#include <vector>

int main() {
    
    int n;
    std::vector<int> b;
    std::vector<int> s;

    b.reserve(10000);
    s.reserve(10000);

    std::cin >> n;
    while (n != 0) {
        b.resize(n);
        for (int i = 0; i < n; ++i) { std::cin >> b[i]; }
        
        s.resize(n);
        s[0] = b[0];
        for (int i = 1; i < n; ++i) { s[i] = s[i - 1] + b[i]; }

        int result = b[0];
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                result = std::max(result, s[j] - s[i] + b[i]);
            }
        }

        if (result <= 0) {
            std::cout << "Losing streak." << std::endl;
        }
        else {
            std::cout << "The maximum winning streak is " << result << "." << std::endl;
        }
        
        std::cin >> n;
    }

    return 0;
}
