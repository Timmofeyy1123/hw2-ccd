import argparse
from astropy.io import fits
from lsp import lstsq
def main():
    
    n, m = 500, 20  
    num_samples = 10000  


    A = np.random.normal(size=(n, m))
    x_true = np.random.normal(size=(m,))


    
    sigma = 0.01
    b_samples = np.random.multivariate_normal(
        mean=np.dot(A, x_true),
        cov=np.eye(n) * sigma**2,
        size=num_samples
    )

    
    costs = [lstsq(A, b)[1] for b in b_samples]


    plt.hist(costs, density=True, bins=50, alpha=0.6, label='Гистограмма величины невязки')


    df = n - m
    x = np.linspace(chi2.ppf(0.01, df), chi2.ppf(0.99, df), 100)


    
    plt.plot(x * (sigma ** 2), chi2.pdf(x, df) / (sigma ** 2), 'r-', linewidth=5, alpha=0.6,
             label='Теоретическое распределение')


    plt.xlabel("x")
    plt.ylabel("Плотность распределения частот")
    plt.legend()
    plt.savefig('chi2.png')
    plt.show()
if __name__ == "__main__":
    args = parser.parse_args()
    print(args.filename)
