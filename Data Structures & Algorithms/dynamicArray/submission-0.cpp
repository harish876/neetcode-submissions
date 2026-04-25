class DynamicArray {
private:
    int *arr = nullptr;
    int len;
    int cap;
public:
    DynamicArray(int capacity) {
        cap = capacity;
        len = 0;
        arr = (int *)malloc(cap * sizeof(int));
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        len+=1;
        if(len > cap){
            resize();
        }
        arr[len-1] = n;
    }

    int popback() {
        int element = arr[len-1];
        arr[len-1] = -1;
        len--;
        return element;
    }

    void resize() {
        arr = (int *)realloc(arr,cap * 2 * sizeof(int));
        cap *= 2;
        return;
    }

    int getSize() {
        return len;
    }

    int getCapacity() {
        return cap;
    }
};
