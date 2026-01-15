### How to setup a folder so that you can start working with Anaconda - Jupyter Lab.
1. Open Anaconda Prompt
2. Select a folder where you want to operate you project.
3. Run following commands in the order mentioned:
    1. `conda activate`
    2. `conda install jupyterlab`
    3. `jupter lab`
4. Now you can open vs code and also work over their.
5. If we instead of `Anaconda` use the normal Python software for programming so we can install `numpy` using `pip install numpy`.

### Introduction to NumPy
1. Numpy Stands for Numerical Python
2. It's a python library used for numerical computing. 
3. It provides tools for working efficiently with arrays, matrices and mathematical functions.
4. NumPy introduces a new data structure called the `ndarray` (n-dimensional array), which is faster & more memory-efficient than Python's built in `lists` for numerical operations.

#### Important Features
- Multidimensional Arrays (n-dimensional array):
    - Provides efficient handling and processing of large datasets using 1D, 2D and 3D arrays.
- Mathematical Functions:
    - Offers a wide range of mathematical oprations such as linear algebra operations, Fourier transforms, and random number generation etc.
- Vectorization:
    - Allows operations to be performed on entire arrays without writing explicit loops, resulting in cleaner and faster code.
- Interoperability:
    - Integrates smoothly with libraries like Pandas, Matplotlib, TensorFlow and PyTorch for data analysis and machine learning.

#### NumPy Arrays vs Python Lists
1. Python Lists are `Heterogenous` (Contains different types of data) & Numpy Arrays are `Homogeneous` (Contains only one or same type of data).
2. Python Lists are slower since it contains different types of data & Numpy arrays are faster since it contains only single type of data + It is internally implemented using the low-level programming language C.
3. Python list and a NumPy array may appear similar because both use contiguous memory, but the way they store data is different. In a Python list, the contiguous memory stores only references (pointers) to objects, while the actual elements are stored separately in different memory locations. This allows Python lists to hold heterogeneous data types, but it also makes operations slower because the program must follow pointers to access the values. In contrast, a NumPy array stores the actual data values themselves in a single continuous block of memory, and all elements are of the same data type. This contiguous storage of homogeneous data makes NumPy arrays more memory-efficient and significantly faster for numerical and mathematical operations.
    - Contiguous memory is a block of memory where all elements are stored in consecutive addresses, one after another, with each element’s address differing by the size of the element. For Example: An int array: arr[0] at 1000, arr[1] at 1004, arr[2] at 1008 → addresses are different but consecutive (one after another), so memory is contiguous.
4. Python lists rely on Python’s built-in looping mechanisms to perform operations on elements, which can be slower because each iteration is handled at the Python level. In contrast, NumPy uses vectorized operations that work on entire arrays at once without the need to write explicit loops. These operations are implemented in optimized low-level code, making NumPy significantly faster and more efficient than Python lists for numerical computations.
