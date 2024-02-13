## L2T04: Python packages for Data Science

The file numpy_task.py has corrections for code and also shows the correct code.

1. Addresses why python doesn’t create a two-dimensional array for the code np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float) ? It also writes it the correct way.
2. It shows difference  a = np.array([0, 0, 0]) and a = np.array([[0, 0, 0]])
3. Creates a A 3 by 4 by 4 array is created with arr = np.linspace(1, 48,
48).reshape(3, 4, 4) uses index or slice to obtain the following: 
    ○ 20.0
    ○ [ 9. 10. 11. 12.]
    ○ [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
    ○ [[5. 6.], [21. 22.] [37. 38.]]
    ○ [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
    ○ [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
    ○ [[1. 4.] [45. 48.]]
    ○ [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]

## Installation
1. **Python**: Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/).
2. **Version**: These programs are written in Python 3. Make sure you have Python 3.x installed.

### Clone the Repository
```bash
git clone https://github.com/vswapna3202/L2T04.git  
```

## Running the programs <br>
Navigate to the directory of each Python file
Run Python using python interpreter
```
python numpy_task.py    
```