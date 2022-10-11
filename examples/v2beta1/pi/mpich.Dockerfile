FROM mpich-builder as builder

COPY pi.cc /src/pi.cc
RUN mpic++ /src/pi.cc -o /pi

FROM mpich

COPY --from=builder /pi /home/mpiuser/pi