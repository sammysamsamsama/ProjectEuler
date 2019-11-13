CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: test

test: P3.cpp
	 $(CXX) $(CXXFLAGS) P3.cpp -o test

clean:
	-rm -f *.o *.gch *~ a.out test *.txt

