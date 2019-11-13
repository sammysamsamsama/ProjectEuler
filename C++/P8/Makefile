CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt

solution: P8.cpp
	 $(CXX) $(CXXFLAGS) P8.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

