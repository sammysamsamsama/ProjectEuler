CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: test

test: P6.cpp
	 $(CXX) $(CXXFLAGS) P6.cpp -o test

clean:
	-rm -f *.o *.gch *~ a.out test *.txt

